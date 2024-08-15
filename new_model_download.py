from huggingface_hub import snapshot_download
import huggingface_hub
huggingface_hub.login("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") # token 从 https://huggingface.co/settings/tokens 获取




snapshot_download(
  repo_id="meta-llama/Llama-2-70b-hf",
  local_dir="/home/qkli/huggingface/pretrained_model",
  local_dir_use_symlinks=False,
  proxies={"https": "http://10.6.24.82:7895"},
  ignore_patterns=[ "*.ot", "*.msgpack", "*.onnx","*.pth"]
)