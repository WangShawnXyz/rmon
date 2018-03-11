# rmon
## rmon 是一个 RESTful Web 应用，实现了 Redis 服务器管理和监控信息获取的 API.
## 后续扩展对接微信公众号

- REST API
| 名称 | URL | HTTP方法 | 成功状态码 | 失败状态码 |
| - | - | - | - | - | - |
| 获取服务器列表 | /servers/ | GET | 200 | 500 |
| 创建服务器 | /servers/ | POST | 201 | 400 |
| 获取服务器 | /servers/server_id | GET | 200 | 404 |
| 更新服务器 | /servers/server_id | PUT | 200 | 404/400 |
| 删除服务器 | /servers/server_id | DELETE | 204 | 404 |
| 获取服务器监控数据 | /servers/server_id/metrics | GET | 200 | 404/500 |