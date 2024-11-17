import os
from huggingface_hub import snapshot_download
 
# 使用cache_dir参数，将模型/数据集保存到指定“本地路径”
snapshot_download(repo_id="jovianzm/img2vid-pexels-350k", repo_type="dataset",
                  cache_dir="./jovianzm/img2vid-pexels-350k",
                  local_dir="test",
                  local_dir_use_symlinks=False, resume_download=True,
                  token='hf_**')
