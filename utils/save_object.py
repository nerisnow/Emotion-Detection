import pickle
import os
from emotiondetection.config import config


def save_object(checkpoint_path, folder_name, file_name, object_name):
    """"""

    print("[INFO]: Saving {}".format(file_name))

    if not os.path.exists(os.path.join(config.BASE_DIR, "checkpoints", folder_name)):
        os.makedirs(os.path.join(config.BASE_DIR, "checkpoints", folder_name))

    outfile = open(os.path.join(checkpoint_path, folder_name, f"{file_name}.pkl"), "wb")

    pickle.dump(object_name, outfile)

    return True


if __name__ == "__main__":
    dogs = {"key": 1}
    print(save_object(config.CHECKPOINT_PATH, "kamal", "dogs", dogs))
