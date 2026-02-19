from huggingface_hub import snapshot_download
import os

# 使用国内镜像加速下载
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

print("开始下载模型...")
snapshot_download(
    repo_id="zai-org/AutoGLM-Phone-9B-GPTQ-4bit",
    local_dir="./models/AutoGLM-Phone-9B-4bit",
    local_dir_use_symlinks=False,
    force_download=True
)
print("模型下载完成！")