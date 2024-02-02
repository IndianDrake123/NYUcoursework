import super_secret_module

def is_imposter(lst, corrupter_function):
    corrupted = corrupter_function(lst)
    if lst is corrupted:
        return True
    else:
        return False