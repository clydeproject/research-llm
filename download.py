#download a snapshot of gpt-oss-120b. (light weight that git lfs clone.)
#before running this script make sure :- sudo python3 -m pip install huggingface_hub is ran.
from huggingface_hub import snapshot_download
snapshot_download(repo_id='openai/gpt-oss-120b',
                  local_dir='/var/model-storage/gpt-oss-120b',# path needs to be adjusted.
                  local_dir_use_symlinks=False)