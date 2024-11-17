# from datasets import load_dataset

# ds = load_dataset("Ghaser/Wikipedia-Knowledge-2M",cache_dir="huggingface/dataset")
import os
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

# 设置你想要下载的模型和数据集的名称列表

dataset_names = ['Ghaser/Wikipedia-Knowledge-2M']

save_directory = "./downloaded_datasets"
# 创建一个函数来下载数据集
def download_datasets(dataset_names, save_directory):
    os.makedirs(save_directory, exist_ok=True)
    for dataset_name in dataset_names:
        dataset = load_dataset(dataset_name)
        dataset_save_path = os.path.join(save_directory, dataset_name.replace('/', '_'))
        dataset.save_to_disk(dataset_save_path)
        print(f"Dataset {dataset_name} downloaded and saved to {dataset_save_path}.")

# 调用函数下载模型和数据集
download_datasets(dataset_names,save_directory)
