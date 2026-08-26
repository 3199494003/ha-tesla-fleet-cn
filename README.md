# Tesla Fleet — China Support (中国大陆支持版)

Home Assistant 官方 **Tesla Fleet** 集成不支持中国大陆账号（官方文档明确 "The China region is currently not supported"）。本仓库是该集成的**最小改造版**：只放开官方故意屏蔽的中国区，让中国大陆特斯拉车主也能在 Home Assistant 里连接并控制自己的车辆。

## 改了什么

与官方组件相比，仅三处改动：

| 文件 | 改动 |
| --- | --- |
| `const.py` | 去掉 `REGION_SERVERS` 里对 `"cn"` 的排除（`if region != "cn"`），使中国区重新出现在区域选项里 |
| `const.py` | **OAuth 认证端点改为中国区**：`authorize` 和 `token` 改用 `auth.tesla.cn`（中国区应用在国际端点 `fleet-auth...tesla.com` 会报 `Client authentication failed`） |
| `lib/tesla_fleet_api/` | **打包了修改版的底层库**：`partner_login` / 刷新令牌的 token 交换端点按区域选择，中国区走 `auth.tesla.cn`（原库写死国际地址导致 `cannot_connect`） |
| `strings.json` | 区域下拉新增 `China / 中国大陆` 选项 |
| `config_flow.py` | 中国区选定时，域名注册提示链接指向中国区开发者门户 `developer.tesla.cn` |
| `hacs.json` | **新增 HACS 2.x 必需配置文件**：HACS 按版本下载集成时必须能拉到该文件（缺失会报 `The version X ... can not be used with HACS`） |

底层库 [`tesla-fleet-api`](https://pypi.org/project/tesla-fleet-api/) 原生支持中国区（`SERVERS` 包含 `cn → https://fleet-api.prd.cn.vn.cloud.tesla.cn`），因此无需重写任何逻辑。

## 前置条件

1. 已注册 [developer.tesla.cn](https://developer.tesla.cn) 中国区开发者账号，创建应用并拿到 **Client ID / Client Secret**
2. 应用申请时勾选了车辆命令相关权限（至少 `vehicle_cmds`、`vehicle_charging_cmds`）
3. 有一个**公网 HTTPS 域名**（用于托管 Tesla 要求的公钥，例如 `https://你的域名/.well-known/appspecific/com.tesla.3p.public-key.pem`）

## 安装

本集成覆盖 HA 内置的官方 `tesla_fleet`（`custom_components` 优先级高于内置），无需卸载任何东西。

### 方式一：HACS（推荐）

1. HACS → 右上角 `⋮` → **自定义存储库** → 添加本仓库（分类选 **集成**）
2. HACS → 集成 → 搜索 **Tesla Fleet (China Support)** → 下载
3. 重启 Home Assistant

### 方式二：手动

把 `custom_components/tesla_fleet/` 整个文件夹复制到 HA 配置目录的 `custom_components/` 下，重启 Home Assistant。

## 使用

1. 设置 → 设备与服务 → 添加集成 → 搜 **Tesla Fleet**
2. 授权登录（用你的特斯拉中国账号）后，区域选择 **China / 中国大陆**
3. 按提示输入你的**公网域名**，并按页面提示把公钥文件放到该域名的 `/.well-known/appspecific/com.tesla.3p.public-key.pem`
4. 新车型会在特斯拉 App 里弹出**虚拟钥匙**配对确认，同意即可
5. 完成 — 锁车、空调、哨兵、充电等实体出现在 HA 里

## 注意

- 此 fork 跟随官方 `tesla_fleet` 组件结构，升级官方版本时只需把官方新文件覆盖回本仓库、再保留 `const.py` 的改动即可
- 仅针对中国区测试；其他区域行为与官方一致
