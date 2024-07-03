## Ollama と GPT-SoVITS を使ったストリーミング対話

### クエリを入力し、Ollama からストリーミングレスポンスを取得して、GPT-SoVITS を使用してオーディオを生成します。会話履歴はコンテキストのために保持され、Markdown をサポートします。

[**English**](../../README.md) | [**中文简体**](../cn/README.md) | **日本語** 

![img](https://github.com/RoversX/Ollama-Voice-Agent/assets/85817538/f4f81bad-7a1d-443a-810f-31fe0fb19e00)

## 目次

- [背景](#背景)
- [インストール](#インストール)
- [使用方法](#使用方法)
- [設定](#設定)
- [トラブルシューティング](#トラブルシューティング)
- [貢献](#貢献)
- [ライセンス](#ライセンス)

## 背景

このプロジェクトは、次の2つの主要技術を活用しています：
1. **[Ollama](https://github.com/ollama/ollama)**：ユーザーの入力と会話履歴に基づいて応答を生成するテキスト生成モデル。
2. **[GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS/)**：テキストをリアルタイムで音声に変換するシステムで、ストリーミング音声出力をサポートしています。

これらの技術の統合により、インタラクティブな音声ベースの対話システムが実現し、ストリーミング音声機能を備えています。

これは最も基本的な機能のみを提供するテスト プロジェクトです。必要に応じて langchain やその他の機能を追加できます。

## インストール

1. **リポジトリをクローン**：
   ```bash
   git clone https://github.com/RoversX/Ollama-Voice-Agent.git
   cd Ollama-Voice-Agent
   ```

2. **仮想環境を作成**：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate` を使用
   ```

3. **依存関係をインストール**：
   ```bash
   pip install requests gradio
   ```
   
## 使用方法

1. **アプリケーションを実行**：
   ```bash
   python ollama.py
   ```

2. **Webインターフェイスにアクセス**：
   Webブラウザを開き、`http://localhost:7860`にアクセスします。

3. **システムと対話**：
   - テキストボックスにメッセージを入力し、「送信」を押します。
   - システムは Ollama を使用して応答を生成し、GPT-SoVITS を使用してテキストを音声に変換します。
   - 生成された音声がリアルタイムで再生されます。

## 設定

- **OLLAMA_API_URL**：Ollama API の URL。
- **GPT_SOVITS_API_URL**：GPT-SoVITS API の URL。

これらは `ollama.py` スクリプトで設定できます。

例
```bash
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
GPT_SOVITS_API_URL = "http://127.0.0.1:9880/"
```

**Ollama の開始**

```shell
ollama serve
```

**GPT-SOVITS API の使用**

```shell
python api.py -dr "sample_audio/Samantha.MP3" -dt "If I could paint a dream on the vast canvas of the world, it would shimmer like a star studded sky." -dl "en"
```
https://raw.githubusercontent.com/RVC-Boss/GPT-SoVITS/main/api.py

これらは `ollama.py` スクリプトで設定できます。

### ログとデバッグ

- **ログを表示**：
  アプリケーションはログをコンソールに出力します。エラーメッセージやデバッグ情報がある場合は、コンソールを確認してください。

- **デバッグを有効にする**：
  コードにログステートメントを追加してフローを追跡し、問題を特定します。例えば、`print` ステートメントや `logging` モジュールを使用してメッセージを記録します。

## 貢献

貢献を歓迎します！リポジトリをフォークしてプルリクエストを送信してください。大きな変更については、まず問題を開いて、変更内容を議論してください。

### 貢献手順

1. リポジトリをフォークします。
2. 新しいブランチを作成します（`git checkout -b feature-branch`）。
3. 変更を行います。
4. 変更をコミットします（`git commit -am 'Add new feature'`）。
5. ブランチにプッシュします（`git push origin feature-branch`）。
6. 新しいプルリクエストを作成します。

## ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。
