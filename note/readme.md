# 无线网络与物联网安全课程笔记

## 课程信息

- **课程名称**：无线网络与物联网安全基础（Fundamental of Wireless Network and IoT Security）
- **授课教师**：任奎（Kui Ren）教授
- **学校**：浙江大学
- **院系**：网络空间安全学院 / 计算机科学与技术学院

---

## 笔记目录

### Week 1：课程介绍与基础概念

- [note01-intro.md](note01-intro.md) — 课程介绍与安全基础概念
  - 课程基本信息、教学安排、学术诚信政策
  - 安全的定义、目标（CIA 三要素及扩展）
  - 安全的复杂性、对手类型、策略与机制
  - 安全设计原则

- [note02-wireless.md](note02-wireless.md) — 无线网络概述
  - 无线通信的历史与发展
  - 未来无线网络愿景与挑战
  - 软件定义无线电（SDR）与频谱问题
  - 香农极限讨论
  - 当前/下一代无线系统（5G、WiFi、卫星、蓝牙、ZigBee）
  - 频谱复用与蜂窝系统
  - WiFi 标准演进（802.11b/a/g/n/ac/ax/be）
  - 毫米波大规模 MIMO
  - 新兴系统（Ad-hoc、认知无线电、能量受限、分布式控制）

- [note03-iot.md](note03-iot.md) — 物联网概述
  - 物联网的定义与多学科特性
  - 物联网的起源与历史
  - 设备增长趋势与技术成熟度
  - 物联网四层模型（感知、网络、管理、应用）
  - 应用案例（自动驾驶、智慧物流、环境监测）
  - 科技巨头的战略布局（Google、Tesla、Apple、小米）
  - 智能网联汽车（ICV）详解
  - 未来信息技术场景

### Week 2：无线网络基础

- [note04-wireless-basics.md](note04-wireless-basics.md) — 无线网络技术基础
  - 数字通信基础（调制、编码、信道容量）
  - Nyquist 公式与 Shannon 容量定理
  - 信号传播特性（路径损耗、穿透损耗）
  - 信号衰落与抗衰落技术（分集、均衡、交织）
  - 多址接入技术（FDM、OFDM、TDD/FDD）
  - 扩频技术（DSSS、FHSS）
  - 移动通信网络演进（2G/3G/4G 架构）
  - 移动通信标准与产业链
  - 频谱分配与全球运营商

### Week 3：无线基础与蜂窝网络安全

- [note05-mac.md](note05-mac.md) — 介质访问控制（MAC）协议
  - 信道分割协议（TDMA、FDMA、CDMA）
  - 随机访问协议（ALOHA、Slotted ALOHA、CSMA、CSMA/CD、CSMA/CA）
  - 隐藏终端与显露终端问题
  - 带有 RTS/CTS 的 CSMA/CA
  - 轮流协议（轮询、令牌传递）

- [note05-lte.md](note05-lte.md) — LTE 蜂窝网络安全
  - LTE 网络架构与协议栈
  - LTE 帧结构
  - 信号遮蔽攻击（SigOver）
  - 信令风暴攻击
  - VoLTE 概述与架构
  - ReVoLTE 攻击（密钥重用漏洞）
  - LTE 安全防御措施

### Week 4：WiFi 安全协议

- [note06-wep.md](note06-wep.md) — 有线等效加密协议（WEP）
  - 无线通信安全需求与威胁模型
  - WiFi 安全协议演进（WEP、WPA、WPA2）
  - WEP 协议设计与加解密流程
  - WEP 的根本性缺陷（密钥流重用、弱密钥、弱完整性校验、缺乏密钥管理）
  - 针对 WEP 的经典攻击（暴力破解、FMS 攻击、ChopChop 攻击、分片攻击）
  - WEP 的历史与废弃
  - 无线网络安全的根本挑战
  - WiFi 与 802.11 标准概述

- [note07-wpa.md](note07-wpa.md) — Wi-Fi Protected Access (WPA)
  - WPA 的诞生背景与设计目标
  - TKIP（临时密钥完整性协议）：两阶段密钥混合、加解密流程
  - WPA 两种工作模式（PSK vs Enterprise）
  - WPA-PSK：四次握手认证、密钥层次（PMK、PTK）、PBKDF2 密钥派生
  - WPA-PSK 攻击：离线字典攻击、暴力破解时间成本、彩虹表攻击
  - WPA 企业模式：IEEE 802.1X、RADIUS、EAP 协议栈
  - Michael MIC 算法、IV 序列强制、Beck-Tews 攻击

- [note08-wpa2.md](note08-wpa2.md) — Wi-Fi Protected Access 2（WPA2）
  - WPA2 概述与 RSN（鲁棒安全网络）标准
  - IEEE 802.1X / EAP 认证框架与三方角色
  - 四次握手与密钥层次（PMK → PTK：KCK / KEK / TK）
  - AES-CCMP：计数器模式加密（CTR）+ CBC-MAC 完整性校验
  - WEP / WPA / WPA2 加密机制全面对比
  - WPA2 优势（抗多种攻击、快速漫游/PMK 缓存/预认证）
  - WPA2 局限（物理层攻击、管理帧无保护、MAC 欺骗/去认证攻击）
  - KRACK 密钥重装攻击：nonce 重用原理、攻击步骤与根本教训
  - WPA2 四个运行阶段（能力发现 → 认证 → 密钥管理 → 数据保护）
  - WPA 的诞生背景与设计目标
  - TKIP（临时密钥完整性协议）：两阶段密钥混合、加解密流程
  - WPA 两种工作模式（PSK vs Enterprise）
  - WPA-PSK：四次握手认证、密钥层次（PMK、PTK）、PBKDF2 密钥派生
  - WPA-PSK 攻击：离线字典攻击、暴力破解时间成本、彩虹表攻击
  - WPA 企业模式：IEEE 802.1X、RADIUS、EAP 协议栈
  - 可扩展认证协议（EAP）：EAPoL、RADIUS 封装、认证流程
  - Michael MIC 算法：64 位消息完整性码
  - IV 序列强制：防御重放攻击
  - Beck-Tews 攻击：利用 QoS 多信道绕过重放保护
  - TKIP 的局限性与长期安全标准需求

- [note08-wpa2.md](note08-wpa2.md) — Wi-Fi Protected Access 2（WPA2）
  - WPA2 概述与 RSN（鲁棒安全网络）标准
  - IEEE 802.1X / EAP 认证框架与三方角色
  - 四次握手与密钥层次（PMK → PTK：KCK / KEK / TK）
  - AES-CCMP：计数器模式加密（CTR）+ CBC-MAC 完整性校验
  - WEP / WPA / WPA2 加密机制全面对比
  - WPA2 优势（抗多种攻击、快速漫游/PMK 缓存/预认证）
  - WPA2 局限（物理层攻击、管理帧无保护、MAC 欺骗/去认证攻击）
  - KRACK 密钥重装攻击：nonce 重用原理、攻击步骤与根本教训
  - WPA2 四个运行阶段（能力发现 → 认证 → 密钥管理 → 数据保护）

### Week 5：RFID 安全与隐私

- [note09-rfid.md](note09-rfid.md) — RFID 安全与隐私
  - RFID 基础概念与三大组成（阅读器、标签、天线）
  - RFID 标签类型（只读/读写）与调制技术（AM/FSK/PSK）
  - 阅读器功能、分类与射频模块（电感耦合/反向散射耦合）
  - RFID 应用场景与愿景、优势与现实挑战
  - RFID 安全威胁：隐私泄露、追踪、认证伪造、企业间谍
  - **GenePrint**：UHF RFID 标签物理层指纹识别（Cov-based 特征、99%+ 准确率）
  - **Hu-Fu**：基于感应耦合和信号随机化的抗重放认证
  - **RF-Mehndi**：指尖轮廓射频标识（INFOCOM 2019 最佳论文，>99% 准确率）
  - **RF-Cloak**：随机化阅读器信号抗 MIMO 窃听
  - 防冲突协议：ALOHA（纯/时隙/帧时隙）、二进制树（查询/随机）
  - **HB/HB+ 协议**：基于 LPN 问题的轻量级认证
  - 隐私保护解决方案：Kill、重命名、距离测量、政策法规

- [note10-nfc.md](note10-nfc.md) — NFC 安全
  - NFC 基础概念（13.56 MHz、4-10 cm、三种工作模式）
  - NFC Forum 四种标签类型（Type 1-4）对比
  - NFC 协议本身的安全空白与 NDEF Signature 克隆漏洞
  - 标签安全分级（Ultralight → Ultralight C → DESFire → 智能卡）
  - NDEF 数据交换格式与 Signature RTD
  - 帧等待时间（FWT）：定义、ATS/FWI 参数、实现缺陷
  - NFC 中继攻击（Relay Attack）：原理、恶意 App 中继、对策困境
  - 手机 NFC 威胁：DoS、恶意软件投递、USSD 攻击
  - Google Wallet PIN 存储漏洞案例分析
  - 可信执行环境（TEE）与安全元件（SE：SIM/嵌入式/MicroSD/HCE）
  - TSM 可信服务管理器与 HCE 主机卡模拟
  - NFC 应用场景：UID 访问控制、事件票务、公交票务、开放支付票务

### Week 6：蓝牙安全与隐私

- [note11-bluetooth.md](note11-bluetooth.md) — 蓝牙安全与隐私（Bluetooth Security and Privacy）
  - 蓝牙概述：ISM 2.4 GHz、个人局域网（PAN）、SIG 管理、命名由来与应用场景
  - 蓝牙技术特征：TDMA-TDD-慢速跳频扩频、10/100 m 范围、微微网容量
  - 网络拓扑：微微网（Piconet，1 主 + 7 活动从）、散射网（Scatternet）规则
  - 物理层机制：79 频率伪随机跳频、自适应跳频（AFH）、625 μs 时隙、TDD
  - 蓝牙版本演进：v1→v5；BLE（v4.0）低功耗、不向下兼容、3 广播 + 37 数据信道
  - 蓝牙安全架构：认证/机密性/授权三目标；Mode 1/2/3 三种安全模式
  - 链路级安全：PIN、BD_ADDR、RAND、E0 流密码、挑战-应答机制
  - 安全威胁：DoS、Fuzzing、Bluejacking、Bluesnarfing
  - 嗅探攻击：CC2540 + PACKET-SNIFFER、ubertooth、libbtbb、wireshark、crackle
  - BLE 重放攻击（Light Blue）与 BLE 配对降级攻击（USENIX Security 2020）
  - BLE 隐私失效：地址随机化质量差、名称泄露、一致地址 → 追踪/画像/伤害用户
  - **BLE-Guardian**（USENIX Security 2016）：学习广播序列精准干扰 + OOB 授权 + 连接参数过滤

### Week 7：物联网安全威胁与防御

- [note12-iot-security.md](note12-iot-security.md) — 物联网安全威胁与防御
  - 物联网发展历程：从 WSN 到 AIoT（1990s-2026）
  - 物联网四层架构：感知层、网络层、管理层、应用层
  - 硬件组件详解：传感器、微处理器、通信芯片、能源供应
  - 最新技术趋势（2024-2026）：MEMS、毫米波雷达、超低功耗 MCU、LoRa Plus、Matter 协议
  - 物联网成为信息安全重灾区：攻击案例、经济损失预测、威胁态势演进
  - 金融行业攻击案例：Carbanak 十亿美元劫案、俄罗斯银行 DDoS、大规模僵尸网络（RCtea、Aisuru）
  - 物联网设备风险等级：灾难性（安防系统、能源计量表）、破坏性（视频会议、打印机、VoIP）、有害性（智能灯泡）
  - 物联网安全需求：接入安全、通信安全、数据隐私安全、计算系统安全
  - 物联网安全架构：感知安全、传输安全、数据安全、应用安全、安全控制与审计
  - 语音助手对抗样本攻击：PhoneyTalker（音素级攻击）、PhyTalker（物理域实时攻击）
  - AIGC 时代新威胁：语音克隆技术评估、5 种克隆技术、攻击有效性分析、检测方法局限
  - 对抗样本的双面性：从威胁到隐私保护工具、非侵入式说话人去识别方案

---

## 学习建议

1. **系统性学习**：三个讲座内容环环相扣，建议按顺序阅读
2. **关注实际应用**：物联网部分包含大量实际案例，可结合新闻和产品了解最新发展
3. **理解基础概念**：安全三要素（机密性、完整性、可用性）是后续学习的基础
4. **掌握技术演进**：WiFi 和蜂窝网络的演进体现了无线通信技术的发展趋势

---

## 重要概念索引

### 安全相关
- CIA 三要素：机密性（Confidentiality）、完整性（Integrity）、可用性（Availability）
- 真实性（Authenticity）、访问控制（Access Control）、不可否认性（Non-repudiability）
- 对手类型：被动/主动、内部/外部
- 安全策略（Policy）vs 机制（Mechanisms）

### 无线网络
- 软件定义无线电（SDR）
- 香农极限（Shannon Limit）
- 频谱复用（Spectral Reuse）
- 蜂窝系统、WiFi 标准（802.11系列）
- 5G 特性、毫米波、大规模 MIMO
- 认知无线电（Cognitive Radio）
- Nyquist 公式、Shannon 容量定理
- 信噪比（SNR）、路径损耗
- 多径衰落、分集技术（Diversity）
- 均衡（Equalization）、交织（Interleaving）
- 频分复用（FDM）、正交频分复用（OFDM）
- 时分双工（TDD）、频分双工（FDD）
- 直接序列扩频（DSSS）、跳频扩频（FHSS）
- 介质访问控制（MAC）协议
- 时分多址（TDMA）、频分多址（FDMA）、码分多址（CDMA）
- 载波监听多路访问（CSMA）
- CSMA/CD（碰撞检测）、CSMA/CA（碰撞避免）
- 隐藏终端（Hidden Node）、显露终端（Exposed Node）
- RTS/CTS 握手机制

### LTE 与蜂窝网络安全
- LTE 网络架构（UE、eNodeB、MME、S-GW、P-GW）
- LTE 协议栈（RRC、PDCP、RLC、MAC、PHY）
- LTE 帧结构（帧、子帧、时隙、OFDM 符号）
- 信号捕捉效应（Capture Effect）
- 信号遮蔽攻击（SigOver Attack）
- 信令风暴攻击
- VoLTE（Voice over LTE）
- IMS（IP Multimedia Subsystem）
- Bearer（承载）
- 流加密（Stream Cipher）
- EEA（EPS Encryption Algorithm）
- ReVoLTE 攻击（密钥重用）
- GPSDO（GPS Disciplined Oscillator）

### WiFi 安全
- WEP（Wired Equivalent Privacy）
- RC4 流密码
- 初始化向量（IV, Initialization Vector）
- CRC-32（循环冗余校验）
- 密钥流重用（Keystream Reuse）
- 弱密钥（Weak Keys）与弱 IV（Weak IVs）
- FMS 攻击（Fluhrer-Martin-Shamir Attack）
- ChopChop 攻击
- 分片攻击（Fragmentation Attack）
- LLC/SNAP 头部
- WPA（Wi-Fi Protected Access）
- TKIP（Temporal Key Integrity Protocol，临时密钥完整性协议）
- 两阶段密钥混合（Phase 1 + Phase 2）
- 成对主密钥（PMK, Pairwise Master Key）
- 成对瞬时密钥（PTK, Pairwise Transient Key）
- PBKDF2（Password-Based Key Derivation Function 2）
- 四次握手（4-Way Handshake）
- WPA-PSK（Pre-Shared Key Mode）
- WPA 企业模式（Enterprise Mode）
- IEEE 802.1X（基于端口的网络访问控制）
- RADIUS（Remote Authentication Dial-In User Service）
- EAP（Extensible Authentication Protocol，可扩展认证协议）
- EAPoL（EAP over LAN）
- Supplicant（请求者）、Authenticator（认证器）、Authentication Server（认证服务器）
- Michael MIC（消息完整性代码）
- IV 序列强制（IV Sequence Enforcement）
- TSC（Temporal Sequence Counter，时间序列计数器）
- Beck-Tews 攻击
- QoS（Quality of Service，服务质量）
- 彩虹表（Rainbow Table）
- 字典攻击（Dictionary Attack）
- WPA2、WPA3
- AES-CCMP
- 管理帧保护（PMF, Protected Management Frames）

### 物联网
- 信息物理系统（Cyber-Physical Systems, CPS）
- 物联网四层模型
- RFID、无线传感器网络
- 智能网联汽车（ICV）
- 自动驾驶三大功能：感知、预测、规划
- 车联网：V2V、V2I、V2C、V2P

### RFID 安全与隐私
- RFID（Radio-Frequency Identification，射频识别）
- 阅读器（Reader / Interrogator）、标签（Tag / Transponder）
- 电感耦合（Inductive Coupling）
- 电磁反向散射耦合（Backscatter Coupling）
- 负载调制（Load Modulation）
- LF（低频）、HF（高频）、UHF（超高频）
- 幅移键控（AM）、频移键控（FSK）、相移键控（PSK）
- 物理层识别（Physical-layer Identification）
- GenePrint（UHF RFID 指纹识别）
- 协方差特征（Covariance-based Feature）
- 等宽直方图法（Equi-width Histogram）
- Hu-Fu（抗重放 RFID 认证）
- 电感耦合感应（Inductive Coupling between Tags）
- 信号随机化（Signal Randomization）
- 标签伪造攻击（Tag Counterfeiting）
- 信号重放攻击（Signal Replay）
- 信号补偿攻击（Signal Compensation）
- RF-Mehndi（指尖射频标识）
- PDoT（Phase Difference of Tags，标签相位差）
- 相位偏移算法（Phase Shifting Algorithm）
- RF-Cloak（RFID 抗窃听系统）
- MIMO 窃听者（MIMO Eavesdropper）
- 一次性密码本（One-time Pad）
- 防冲突协议（Anti-collision Protocol）
- ALOHA 协议：纯 ALOHA、时隙 ALOHA（S-ALOHA）
- 帧时隙 ALOHA（FSA, Framed Slotted ALOHA）
- Q 算法（动态帧长调整）
- 标签饿死（Tag Starvation）
- 查询二进制树（Query Binary Tree）
- 随机二进制树（Random Binary Tree）
- HB 协议 / HB+ 协议（Hopper-Blum Protocol）
- LPN 问题（Learning Parity with Noise）
- 内积（Inner Product）、奇偶性（Parity）
- 盲化值（Blinding Value）
- EPC Gen2 标准
- Kill 命令（标签销毁）

---

## 更新日志

- 2026-06-21：创建 Week 1 笔记（note01-intro、note02-wireless、note03-iot），涵盖课程介绍、安全基础、无线网络概述和物联网概述
- 2026-06-21：创建 Week 2 笔记（note04-wireless-basics），涵盖无线网络技术基础，包括数字通信、信道容量理论、信号传播与衰落、多址接入技术、扩频技术以及移动通信网络演进
- 2026-06-22：创建 Week 3 笔记，拆分为 note05-mac（MAC 协议）与 note05-lte（LTE 蜂窝网络安全）
- 2026-06-22：创建 Week 4 笔记（note06-wep），深入分析 WEP 的设计缺陷与攻击方法
- 2026-06-22：创建 Week 4 笔记（note07-wpa），全面讲解 WPA 协议
- 2026-06-22：创建 Week 4 笔记（note08-wpa2），深入分析 WPA2 及 KRACK 密钥重装攻击
- 2026-06-22：创建 Week 5 笔记（note09-rfid），全面讲解 RFID 安全与隐私，包括物理层认证技术（GenePrint、Hu-Fu、RF-Mehndi、RF-Cloak）、防冲突协议（ALOHA/二进制树）、轻量级认证（HB/HB+）和隐私保护方案


