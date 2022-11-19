from aim import Run

# Initialize a new run
run = Run(repo='aim://0.0.0.0:43800')

# Log run parameters
run["hparams"] = {
    "learning_rate": 0.001,
    "batch_size": 32
}

# Log metrics
for i in range(10):
    run.track(i, name='loss', step=i, context={ "subset":"train" })
    run.track(i, name='acc', step=i, context={ "subset":"train" })
