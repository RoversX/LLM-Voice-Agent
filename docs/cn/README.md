## 使用 Ollama 和 GPT-SoVITS 进行流式对话

### 输入您的查询，从 Ollama 获取流式响应，并使用 GPT-SoVITS 生成音频。会话历史会保留以供上下文参考，支持 Markdown。

[**English**]((./README.md)) | **中文简体** | [**日本語**](./docs/ja/README.md)

![img](https://github.com/RoversX/Ollama-Voice-Agent/assets/85817538/f4f81bad-7a1d-443a-810f-31fe0fb19e00)

## 目录

- [背景](#背景)
- [安装](#安装)
- [使用](#使用)
- [配置](#配置)
- [故障排除](#故障排除)
- [贡献](#贡献)
- [许可证](#许可证)

## 背景

该项目利用了两项关键技术：
1. **[Ollama](https://github.com/ollama/ollama)**：一个基于用户输入和会话历史生成响应的文本生成模型。
2. **[GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS/)**：一个将文本实时转换为音频的系统，支持流式音频输出。

这些技术的集成实现了一个互动的、基于语音的对话系统，并具有流式音频能力。

## 安装

1. **克隆仓库**：
   ```bash
   git clone https://github.com/RoversX/Ollama-Voice-Agent.git
   cd Ollama-Voice-Agent
   ```

2. **创建虚拟环境**：
   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上，使用 `venv\Scripts\activate`
   ```

3. **安装依赖**：
   ```bash
   pip install requests gradio
   ```
   
## 使用

1. **运行应用程序**：
   ```bash
   python ollama.py
   ```

2. **访问 Web 界面**：
   打开您的 Web 浏览器并访问 `http://localhost:7860`。

3. **与系统互动**：
   - 在文本框中输入您的消息并按“发送”。
   - 系统将使用 Ollama 生成响应，并使用 GPT-SoVITS 将文本转换为音频。
   - 生成的音频将实时播放。

## 配置

- **OLLAMA_API_URL**：Ollama API 的 URL。
- **GPT_SOVITS_API_URL**：GPT-SoVITS API 的 URL。

这些可以在 `ollama.py` 脚本中配置。

示例
```bash
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
GPT_SOVITS_API_URL = "http://127.0.0.1:9880/"
```

**启动 Ollama**

```shell
ollama serve
```

**使用 GPT-SOVITS API**

```shell
python api.py -dr "sample_audio/Samantha.MP3" -dt "If I could paint a dream on the vast canvas of the world, it would shimmer like a star studded sky." -dl "en"
```
https://raw.githubusercontent.com/RVC-Boss/GPT-SoVITS/main/api.py

这些可以在 `ollama.py` 脚本中配置。

### 日志和调试

- **查看日志**：
  应用程序将日志输出到控制台。请检查控制台以获取任何错误消息或调试信息。

- **启用调试**：
  在代码中添加日志语句以跟踪流程并识别问题。例如，使用 `print` 语句或 `logging` 模块记录消息。

## 贡献

我们欢迎贡献！请分叉仓库并提交拉取请求。对于重大更改，请首先打开一个问题以讨论您想要更改的内容。

### 贡献步骤

1. 分叉仓库。
2. 创建一个新分支（`git checkout -b feature-branch`）。
3. 进行更改。
4. 提交更改（`git commit -am 'Add new feature'`）。
5. 推送到分支（`git push origin feature-branch`）。
6. 创建一个新的拉取请求。

## 许可证

该项目根据 MIT 许可证获得许可。
