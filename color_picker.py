import cv2
import numpy
from sklearn.cluster import KMeans

class ColorPicker:
    # using histogram of the colors to find the most common ones
    def make_histogram(self, cluster):
        labels_count = numpy.arange(0, len(numpy.unique(cluster.labels_)) + 1)
        hist, _ = numpy.histogram(cluster.labels_, bins=labels_count)
        hist = hist.astype('float32')
        hist /= hist.sum()

        return hist

    def get_rgb(self, array):
        red, green, blue = int(array[2]), int(array[1]), int(array[0])
        return (red, green, blue)
    
    def rgb_to_hex(self, rgb):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    def get_colors(self, file, colors_count):
        image = cv2.imdecode(numpy.frombuffer(file.read(), numpy.uint8), cv2.IMREAD_COLOR)

        # resize image
        image = cv2.resize(image, (10, 10), interpolation = cv2.INTER_AREA)

        height, width, _ = numpy.shape(image)
        img = image.reshape((height * width, 3))

        # most common cluster (colors) 
        clusters_count = colors_count
        clusters = KMeans(n_clusters=clusters_count)
        clusters.fit(img)

        # make histogram
        histogram = self.make_histogram(clusters)

        #sort by most common
        combined = zip(histogram, clusters.cluster_centers_)
        combined = sorted(combined, key=lambda x: x[0], reverse=True)

        colors_with_frequencies = {}

        for index, rows in enumerate(combined):
            rgb = self.get_rgb(rows[1])
            hex = self.rgb_to_hex(rgb)
            colors_with_frequencies[str(index)] = {"rgb": rgb, "hex": hex}

        return colors_with_frequencies