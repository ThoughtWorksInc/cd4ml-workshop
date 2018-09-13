# Continuous Intelligence Workshop

## Running Workshop with dvc

1. Build the pipline
2. Push the results
3. Pull and reproduce

### Build Pipeline with dvc

```sh
dvc run -d src/download_data.py -d gs://continuous-intelligence/store47-2016.csv -o data/raw/store47-2016.csv python src/download_data.py
dvc run -d data/raw/store47-2016.csv -d src/splitter.py -o data/splitter/train.csv -o data/splitter/validation.csv python src/splitter.py
dvc run -d data/splitter/train.csv -d data/splitter/validation.csv -d src/decision_tree.py -o data/decision_tree/model.pkl -M results/score.txt python src/decision_tree.py
```

### Push the Results

First, push code changes to Github as usual, for instance:
```sh
git commit -am "Change model to be more awesome"
git push origin master
```

Next, push your dvc files to the cloud:
```sh
dvc push
```

That's it! Now anyone with access can fetch this repository and use dvc to replicate and build on your work.

### Pull and reproduce changes

First, clone/pull this git repo.

```sh
git pull origin master --rebase
```

Next, pull from the cloud with dvc:
```sh
dvc pull
```

Finally, to reproduce the entire pipeline, simply run:
```sh
dvc repro model.pkl.dvc
```
Here, `model.pkl.dvc` is the last output in the dvc pipeline. Running it will reproduce all steps.

If you want to change the model, for example, edit the `decision_tree.py` file as you see fit. Then, you should be able to re-execute the model simply by re-running the pipeline using `dvc repro model.pkl.dvc`.

## Local setup

### Build locally and run

Once the model has been trained

`docker build . -t ci-workshop`

`docker run -d -p 5005:5005 ci-workshop`

You can view the app at `http://localhost:5005`

Note: try to assign 8G memory and 2CPU in Docker when running the docker build

### Run with existing image

`docker pull TBD`

`docker run -d -p 5005:5005 TBD`
