# Lecture 11：Wi-Fi Protected Access 2（WPA2）

> 本讲在 WPA/TKIP 的基础上，介绍以 IEEE 802.11i 为标准、以 AES-CCMP 为核心的 WPA2 协议，
> 并详细分析 2017 年曝光的 KRACK 密钥重装攻击。

---

## 一、WPA2 概述 (page 12)

Wi-Fi Protected Access 2（WPA2）基于 IEEE 802.11i 标准，是 WPA/TKIP 的正式继任者。它引入了基于 AES 的加密套件 CCMP，将安全性提升到全新层次。802.11i 最终形态称为**鲁棒安全网络（RSN，Robust Security Network）**。

WPA2 的核心改进：
- 使用 **AES（Advanced Encryption Standard）** 替代 RC4，密钥长度 128 位。
- 引入 **Counter-Mode/CBC-MAC Protocol（CCMP）** 同时保证机密性与完整性。
- 保留并完善了 WPA 的四次握手与 802.1X/EAP 认证框架。

### WPA2 两种工作模式 (page 23)

| 模式 | 认证方式 | 适用场景 |
| :---: | :---: | :---: |
| **Personal（个人模式）** | PSK（预共享密钥） | 家庭/小型网络 |
| **Enterprise（企业模式）** | 802.1X + EAP | 企业/校园网络 |

---

## 二、认证框架：IEEE 802.1X 与 EAP (page 2-4)

### 认证三方角色 (page 2)

WPA2 企业模式的认证涉及三个角色：

- **请求者（Supplicant，STA）**：希望接入网络的终端设备。
- **认证器（Authenticator，AP）**：接入点，负责中转认证消息。
- **认证服务器（Authentication Server，AS）**：通常是 RADIUS 服务器，执行实际认证。

### 认证三个阶段 (page 2)

1. **连接到 AS**：STA 向关联的 AP 发送接入请求，AP 转发给 AS。
2. **EAP 交换**：STA 与 AS 相互认证。
3. **安全密钥传递**：认证完成后，AS 生成**主会话密钥（Master Session Key）**并下发给 STA。

### EAP 交换详细流程 (page 3)

> [!tip]+ EAP 认证步骤
>
> 1. STA 发送 **EAPOL-Start** 消息，启动 802.1X 交换。
> 2. AP（认证器）向 STA 发送 **EAP-Request/Identity** 帧，请求身份标识。
> 3. STA 回复 **EAP-Response/Identity** 帧，AP 将其转发给 RADIUS 服务器。
> 4. RADIUS 服务器确定所需认证方法，发送 **EAP-Request/Method** 帧。
> 5. STA 回复 **EAP-Response/Method** 帧。
> 6. 步骤 4-5 重复执行，完成完整认证。
> 7. RADIUS 服务器发送 **Radius-Access-Accept** 数据包，授权接入。

### 第三阶段：密钥管理 (page 4)

- AS 将 **PMK（Pairwise Master Key，成对主密钥）** 发送给 AP（认证器）。
- STA 和 AP 现在持有相同的 PMK，PMK 在整个会话期间保持不变。
- PMK 本身不直接用于数据加密，需通过**四次握手**派生 **PTK（Pairwise Transient Key，成对瞬时密钥）**。

---

## 三、四次握手与密钥层次 (page 5-8)

### 四次握手的目的 (page 5)

> [!definition]+ 四次握手（4-Way Handshake）
>
> 四次握手是 WPA/WPA2 中用于双方协商并安装加密密钥的核心机制，完成以下任务：
>
> 1. 确认客户端持有正确的 PMK。
> 2. 确认 PMK 是最新有效的。
> 3. 从 PMK 派生 **PTK（成对瞬时密钥）**。
> 4. 将成对加密密钥和完整性密钥安装到 IEEE 802.11。
> 5. 将 **GTK（Group Temporal Key，组临时密钥）** 及其序列号从 AP 传递给 STA 并安装。
> 6. 确认密码套件的选择。

PTK 的计算公式为：

$$\text{PTK} = \text{Combine}(\text{PMK},\ \text{ANonce},\ \text{SNonce})$$

其中 ANonce 由 AP 生成，SNonce 由 STA 生成，两者均为随机数，确保每次会话的 PTK 唯一。

### 成对密钥层次结构 (page 7)

PMK 的来源取决于认证方式：
- **PSK 模式**：PMK 直接等于预共享密钥（PSK）。
- **企业模式**：PMK 由 802.1X 认证产生的 MK（Master Key）派生而来。

密钥层次如下：

```
Master Key (MK) / Pre-Shared Key (PSK)
        │
        ▼
  Pairwise Master Key (PMK)
        │
        ▼
  Pairwise Transient Key (PTK)  [64 字节]
     ├── Key Confirmation Key (KCK)  [16 字节]
     ├── Key Encryption Key (KEK)    [16 字节]
     └── Temporal Key (TK)           [16 字节]
```

### PTK 的三个组成部分 (page 8)

| 子密钥 | 长度 | 用途 |
| :---: | :---: | :---: |
| **KCK**（EAPOL-Key Confirmation Key） | 16 字节 | 计算 WPA EAPOL Key 消息的 MIC（消息完整性码） |
| **KEK**（EAPOL-Key Encryption Key） | 16 字节 | AP 用于加密下发给客户端的附加数据（如 RSN IE、GTK） |
| **TK**（Temporal Key） | 16 字节 | 加解密单播数据包 |

> [!note]+ 为什么需要多层密钥？
>
> PMK 作为长期密钥直接用于加密风险极高——一旦泄露，所有历史通信均可解密。
> 通过四次握手每次协商新的 PTK（包含随机 nonce），即使某次 TK 泄露，
> 其他会话和之前的通信也不受影响，实现了**前向安全性（Forward Secrecy）**的近似效果。

---

## 四、WPA2 加密：AES-CCMP (page 9-14)

### CCMP 概述 (page 9, 12-13)

WPA2 相对于 WPA 最核心的改进是将加密算法从 RC4 替换为 **AES（高级加密标准）**，使用 128 位密钥，通过 **CCMP（Counter-Mode/CBC-MAC Protocol）** 协议同时提供机密性和完整性保护。

CCMP 由两部分组成：
- **CTR 模式（Counter Mode）**：用于数据加密，提供机密性。
- **CBC-MAC（Cipher Block Chaining - Message Authentication Code）**：用于完整性校验。

### 计数器模式加密（CTR Mode）(page 10)

计数器模式是一种将分组密码转换为流密码的工作模式：

> [!example]+ CTR 模式工作原理
>
> - 维护一个不断递增的**计数器（Counter）**。
> - 对每个计数器值用 AES 加密，生成密钥流块（keystream block）。
> - 将密钥流块与明文数据进行 XOR 运算，得到密文。
> - 接收方用相同计数器生成相同密钥流，XOR 密文即可还原明文。
>
> 优势：加密和解密完全相同，且可并行处理；计数器的唯一性确保密钥流不重用。

### CBC-MAC 完整性保护 (page 11)

CBC-MAC 用于验证数据在传输过程中未被篡改：

- 将数据分成 128 位的块。
- 对第一块数据先进行 AES 加密，将结果与下一块数据进行 XOR。
- 重复此过程直到处理完所有数据块，最终产生一个 **MAC（消息认证码）**。
- 接收方执行相同计算，对比 MAC 值验证完整性。

### CCMP 核心特性 (page 14)

1. **头部完整性保护**：CCMP 对 MAC 帧的帧体（frame body）和绝大部分头部（header）都提供完整性保护，防止攻击者篡改 MAC 头部字段。

2. **48 位数据包编号（PN，Packet Number）**：
   - 防御**重放攻击（Replay Attacks）**：接收方维护接收到的最大 PN，拒绝 PN 更小的数据包。
   - 为每个数据包构造唯一的 nonce，避免密钥流重用。

3. **安全性证明**：分析表明，一旦正确实现 CCMP，攻击者在不知道密钥的前提下无法破坏数据机密性和完整性。

---

## 五、WEP / WPA / WPA2 对比 (page 15)

| 特性 | WEP | WPA | WPA2 |
| :---: | :---: | :---: | :---: |
| **加密算法** | RC4 | RC4 | AES |
| **密钥长度** | 40 位 | 128 位（加密）/ 64 位（认证） | 128 位 |
| **密钥生命周期** | 24 位 IV | 48 位 IV | 48 位 IV |
| **数据包密钥** | 直接拼接 | 混合函数（两阶段） | 不需要（由 CTR nonce 保证唯一性） |
| **数据完整性** | CRC-32 | Michael 算法 | CCM |
| **头部完整性** | 无 | Michael 算法 | CCM |
| **抗重放攻击** | 无 | IV 序列强制 | IV 序列强制 |
| **密钥管理** | 无 | 基于 EAP | 基于 EAP |

---

## 六、WPA2 的优势与局限 (page 16-19)

### 优势 (page 16-17)

WPA2 对以下多种攻击具有免疫性：
- 中间人攻击（Man-in-the-middle）
- 认证伪造（Authentication forging）
- 重放攻击（Replay）
- 密钥碰撞（Key collision）
- 弱密钥（Weak keys）
- 数据包伪造（Packet forging）
- 暴力破解 / 字典攻击（Brute-force / Dictionary attacks）

此外，WPA2 支持**快速漫游**：
- **PMK 缓存（PMK Caching）**：客户端重新连接到最近关联过的 AP 时，无需重新完整认证。
- **预认证（Pre-authentication）**：客户端在离开当前 AP 之前，可提前向目标 AP 完成认证，实现无缝切换。

### 局限性 (page 18-19)

WPA2 无法抵御物理层攻击：
- **射频干扰（RF Jamming）**：通过干扰无线信号实现拒绝服务。
- **数据洪泛（Data Flooding）**
- **接入点硬件故障（Access Point Failure）**

控制/管理帧的安全缺陷：
- 管理帧（如 Beacon、Probe、De-authentication）默认**不加密、不认证**，攻击者可从中窥探大量网络信息。
- 容易遭受 **DoS 攻击**（如伪造 De-authentication 帧强制断开客户端）。
- 易受 **MAC 地址欺骗**和**批量去认证攻击（Mass De-authentication Attack）**。

> [!note]+ WPA3 的改进
>
> WPA3 针对上述管理帧漏洞引入了**受保护管理帧（PMF，Protected Management Frames）**（即 IEEE 802.11w），
> 强制保护 De-authentication 和 Disassociation 帧，显著缓解了去认证攻击。

---

## 七、KRACK 攻击：密钥重装攻击 (page 20-33)

### 背景与威胁级别 (page 20)

**KRACK（Key Reinstallation Attack，密钥重装攻击）**由 Mathy Vanhoef 于 2017 年公开披露。

- **目标**：利用 WPA2 四次握手中的漏洞，强迫客户端重装已用过的会话密钥，从而重置 nonce 为初始值。
- **威胁范围**：所有支持 WPA/WPA2 的 Wi-Fi 路由器和设备均受影响。
- **危害**：攻击者可解密加密流量，实施中间人攻击，在某些情况下还可篡改数据。

### 四次握手回顾与安全假设 (page 21-22)

四次握手被长期认为是安全的：
- 超过十年无实际攻击（除密码猜测外）。
- 数学证明了协商的 PTK 是保密的。
- 加密协议本身被证明是安全的。

然而，这些证明都基于各组件独立运行的抽象模型，**没有证明组合后的系统整体安全**。

### nonce 重用的根本危害 (page 26)

CCMP 的安全性依赖于**每个数据包使用唯一的 nonce**：

$$\text{密文} = \text{明文} \oplus \text{AES}(\text{Key},\ \text{nonce})$$

如果相同的 (Key, nonce) 被使用两次：

$$\text{密文}_1 \oplus \text{密文}_2 = \text{明文}_1 \oplus \text{明文}_2$$

攻击者只需截获两段密文，即可通过 XOR 运算得到两段明文的 XOR，配合已知明文（如 ARP 包的格式固定）即可还原数据。

> [!note]+ 这与 WEP 的 IV 重用问题本质相同
>
> WEP 因 IV 空间只有 24 位，必然发生重用。
> WPA2 的 48 位 PN 空间足够大，正常情况下不会重用——
> KRACK 的关键在于**人为强制重置 nonce**，绕过了这个安全设计。

### KRACK 攻击过程 (page 27-33)

> [!example]+ 密钥重装攻击步骤
>
> **正常四次握手流程**：
> - Msg1：AP → STA（ANonce）
> - Msg2：STA → AP（SNonce + MIC）
> - Msg3：AP → STA（GTK + MIC，AP 等待 Msg4）
> - Msg4：STA → AP（确认，PTK 安装，nonce 初始化为 0）
>
> **KRACK 攻击注入**：
>
> 1. 攻击者作为中间人，拦截（Block）STA 发出的 Msg4，AP 未收到确认。
> 2. AP 超时后**重传 Msg3**。
> 3. STA 收到重传的 Msg3，认为 PTK 未安装，再次**重装（reinstall）相同的 PTK**。
> 4. **nonce 被重置为 0**，STA 从 0 开始重新计数发送数据包。
> 5. 此时 STA 用相同的 TK 和重置的 nonce 加密新数据，与之前的密文发生 nonce 重用。
> 6. 攻击者收集到用相同 (TK, nonce) 加密的多段密文，可还原明文。

攻击示意（简化版）：

```
AP                      STA (victim)         Attacker
 |---Msg3 (PTK+GTK)---->|                        |
 |                       |---Msg4 (encrypted)--->|  (blocked!)
 |                       | [PTK installed, nonce=0]
 |  (no Msg4, retransmit)|                        |
 |---Msg3 (retransmit)-->|                        |
 |                       | [PTK reinstalled, nonce RESET to 0]
 |                       |==send data (nonce=1)==>|
 |                  (previously sent nonce=1 data also captured)
 |                  → keystream reuse → decryption possible
```

### 关键教训 (page 35)

> [!important]+ 形式化证明的局限性
>
> - WPA 四次握手已被证明安全。
> - 加密密码已被数学证明安全。
> - **但两者组合并未被证明安全。**
> - 企业模式（802.1X/EAP）与个人模式（PSK）同样脆弱——给人虚假的安全感。
> - **抽象模型 ≠ 真实代码**：必须保证代码与规范完全匹配。
>
> KRACK 的根本教训：密码学组件各自安全，不代表组合后的协议安全；
> 协议设计必须考虑重传、重放等真实网络场景。

---

## 八、WPA2 四个运行阶段 (page 34-40)

WPA2 协议的完整运行分为四个阶段：

### 阶段一：能力发现（Capability Discovery）(page 36-39)

**目标**：AP 与 STA 相互发现并协商安全能力。

1. **Beacon / Probe Response**：AP 广播或响应探测请求，在 **RSN 信息元素（RSN IE，Robust Security Network Information Element）**中宣告其安全能力（支持的认证方式、密码套件等）。

2. **开放系统认证（Open System Authentication）**：
   - 仅用于保持与 IEEE 802.11 旧版状态机的向后兼容性。
   - **不提供任何安全功能**，双方仅交换标识符（MAC 地址）。

3. **关联（Association）**：
   - STA 向 AP 发送 **Association Request** 帧，从 AP 宣告的能力中选择一套匹配的配置：认证与密钥管理套件（AKM）、单播密码套件（Pairwise Cipher Suite）、组密钥密码套件（Group-Key Cipher Suite）。
   - 此阶段完成安全能力的协商与绑定。

### 阶段二：认证（Authentication）(page 40)

基于阶段一协商的 EAP 认证方法，完成 STA 与 AS 的双向认证，并在 AS 与 STA 之间建立 PMK。（具体流程见第二节 EAP 交换。）

### 阶段三：密钥管理（Key Management）

基于 PMK，通过四次握手生成并安装 PTK 和 GTK。（具体流程见第三节。）

### 阶段四：数据保护（Data Protection）

阶段三生成的所有密钥（PTK 中的 TK、GTK）由 **CCMP 协议**使用，为数据通信提供机密性和完整性保护。（具体机制见第四节。）

---

## 九、总结

WPA2 是迄今为止 Wi-Fi 安全标准的重要里程碑：

- **加密强度**大幅提升（RC4 → AES-CCMP），正确实现后数据机密性与完整性有数学保证。
- **认证体系**成熟（802.1X/EAP，支持企业级认证服务器）。
- **协议设计**仍存在组合安全性的盲点，KRACK 攻击揭示了"各部分安全 ≠ 整体安全"的教训。
- WPA3 在此基础上引入 SAE（Simultaneous Authentication of Equals）替代 PSK，从根本上消除了 KRACK 类密钥重装漏洞，并强制保护管理帧。
