from datasets import load_dataset

ds = load_dataset("imagefolder", data_dir=r'C:\Users\user\OneDrive\Masaüstü\test', split="test")

ds_split_train_test = ds.train_test_split(test_size=0.15)

train_ds, test_ds = ds_split_train_test["train"], ds_split_train_test["test"]

ds_split_train_val = train_ds.split_train_test(test_size=0.15/0.85)

train_ds, val_ds = ds_split_train_test["train"], ds_split_train_test["test"]