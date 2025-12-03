# Creat Env in (\C:) Directory

conda create -n {Environment Name} python={Python Version} -y

conda activate {Environment Name}

conda env list

conda remove --name {Environment Name} --all



# Creat Env in another Directory
conda create --prefix .\{Environment Name} python={Python Version} -y

conda activate .\{Environment Name}




pip install {Library Name}=={Library Version}
