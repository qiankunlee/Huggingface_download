import os
from huggingface_hub import snapshot_download


os.environ['HF_ENDPOINT']='https://hf-mirror.com'
# 使用cache_dir参数，将模型/数据集保存到指定“本地路径”
snapshot_download(repo_id="Ghaser/Wikipedia-Knowledge-2M", repo_type="dataset",
                  cache_dir="./Ghaser/Wikipedia-Knowledge-2M",
                  local_dir="test",
                  local_dir_use_symlinks=False, resume_download=True,
                  token='hf_**',
                  )
