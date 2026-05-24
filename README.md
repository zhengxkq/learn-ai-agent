# learn-ai-agent

前端工程师转 AI 应用开发的学习笔记 + 代码实践。

## 当前进度

### W0a · Python 速通（Day 1 + Day 2）

| 文件 | 主题 |
|------|------|
| `diff_demo.py` | JS vs Python 5 个核心差异 |
| `types_demo.py` | 类型提示 + Union |
| `pydantic_demo.py` | Pydantic 自动校验 + 嵌套 Model |
| `chat_message.py` | TS interface 翻译成 Pydantic |
| `async_demo.py` / `async_demo2.py` | 同步 vs 异步对比(4秒 → 2秒) |
| `httpx_demo.py` | 异步 HTTP 请求 |
| `httpx_concurrent.py` / `httpx_sequential.py` | 并发 vs 串行对比 |
| `llm_hello.py` | 调用大模型 API(阿里云 Coding Plan) |
| `llm_stream.py` | 流式输出 |

## 配套文章

- [JS 党转 Python:80% 语法免费,但这 20% 让我栽了](#)（待补链接）
- [7 年前端,我用半天把 Python AI 开发跑通了](#)（待补链接）

## 运行

```bash
uv sync
cp .env.example .env  # 填入你自己的 DASHSCOPE_API_KEY
uv run llm_hello.py