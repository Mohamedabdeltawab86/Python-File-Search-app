import os


def find_file(filename):
    results = []
    for root, dir, files in os.walk('E:'):
        if filename in files:
            results.append(os.path.join(root, filename))
    return results


print(find_file("musculoskeletal FINAL2.xls"))
