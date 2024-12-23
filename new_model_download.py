from huggingface_hub import snapshot_download
import huggingface_hub
huggingface_hub.login("") # token 从 https://huggingface.co/settings/tokens 获取


os.environ['HF_ENDPOINT']='https://hf-mirror.com'

snapshot_download(
  repo_id="meta-llama/Llama-2-70b-hf",
  local_dir="huggingface/pretrained_model",
  local_dir_use_symlinks=False,
  proxies={"https": "http://"},
  ignore_patterns=[ "*.ot", "*.msgpack", "*.onnx","*.pth"]
)
