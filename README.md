# OncoMetric Nexus

## project description


You will need to build a complete data operations pipeline. We need to collect
data from an external source, prepare them for a machine learning experience,
run such an experience, and reconcile the results of the experience in a way
that could be shared with other researchers. There are 5 tasks.

1. You need to get the data from the CMMD dataset. The dataset is available on
   the Cancer Imaging Archive website
[here](https://www.cancerimagingarchive.net). We need a tool that collects the
data in an automated manner. We might not need or be able to download the whole
dataset, so your code should be allowed to process a portion of it.

    - Bonus: wrapping the tools in Docker container will be useful.

2. Once the images and the provided clinical data are downloaded, you need to
   prepare the dataset for the deep learning experiments. First, you should
structure the data in a way to allow them to be used and queried effectively.
You are free to choose any manner that you find appropriate.

3. Next, we need a code that would split data in a consistent and reproducible
   manner. You need to choose an appropriate splitting strategy. In this
assignment, our main target would be to train a classifier to separate benign
and malignant samples.

4. Now we need to run a deep-learning experiment. Note that we are not
   necessarily looking for the performances, but for the experiment as part of
the pipeline. Your code should be able to read input data that are split
according to the strategy defined in the previous step. The result of the
experiments shall be reusable and sharable metrics.

    - Bonus 1: The DICOM data might not be the most optimal for running
    experiments, so you can implement a pipeline step that would preprocess and
    store the images in a different format.

    - Bonus 2: While the main target of our experiment is separating benign and
    malignant samples, you are free to introduce other classification tasks of
    your choice (e.g., type of abnormality)

5. Finally, we want the generated metrics to be shared with others. There are
   plenty of tools for the job, and you are free to use any that you find the
most appropriate.

Please keep in mind a few things:

- There's a myriad of frameworks and tools, but if you opt for a neural network
we would prefer if you used Python as programming language, Docker for
containerization, and Tensorflow for deep learning.

- While building Docker container is explicitly stated as Bonus in the first
task, it is applicable to all the other tasks as well.

- While the deep learning experiments are not in the main scope of this
assignment, you are free to dive as deep as you want.

- You are expected to use a code repository (private GitLab or GitHub
repository is fine) and commit the code carefully. Your code should be
comprehensive. Please comment when needed.

Your deliverables shall include:

- Source codes;
- build and execution instructions;
- file of files with metrics and illustrations;
- any additional instructions you judge necessary.

Note, that while the metrics are part of the deliverables, your work is not
evaluated by the level of the obtained performances.
