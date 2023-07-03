import cv2;
import numpy
from sklearn.cluster import KMeans

# using histogram of the colors to find the most common ones
def make_histogram(cluster):
    labels_count = numpy.arange(0, len(numpy.unique(cluster.labels_)) + 1)
    hist, _ = numpy.histogram(cluster.labels_, bins=labels_count)
    hist = hist.astype('float32')
    hist /= hist.sum()

    return hist

# display n colors
def make_bar(height, width, color):
    bar = numpy.zeros((height, width, 3), numpy.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])

    return bar, (red, green, blue)

def get_colors(image, colors):
    # image read and reshape
    image = cv2.imread(image)
    height, width, _ = numpy.shape(image)
    img = image.reshape((height * width, 3))

    # most common cluster (colors) 
    clusters_count = colors
    clusters = KMeans(n_clusters=clusters_count)
    clusters.fit(img)

    # make histogram
    histogram = make_histogram(clusters)

    #sort by most common
    combined = zip(histogram, clusters.cluster_centers_)
    combined = sorted(combined, key=lambda x: x[0], reverse=True)

    # output colors
    bars = []
    for index, rows in enumerate(combined):
        bar, rgb = make_bar(100, 100, rows[1])
        print(f'Color {index + 1}')
        print(f'Values: {rgb}')
        bars.append(bar)

    cv2.imshow(f'{clusters_count} most common colors', numpy.hstack(bars))
    cv2.waitKey(0)

get_colors('C:/Users/karab/Downloads/download.jpg', 3)