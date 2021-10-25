import installers as i


def run_all():
    for j in dir(i):
        item = getattr(i, j)
        if callable(item):
            item()


if __name__ == "__main__":
    run_all()

# I will be making this a lot better becuase this is real useful for me
