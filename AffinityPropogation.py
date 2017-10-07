import contextlib

class AffinityPropogation(object):
    num_iterations = 100

    def __init__(self, data_points):
        self.lam = 0.9
        self.num_cols_and_rows = len(data_points)
        self.similarities = [[0 for x in range(self.num_cols_and_rows)] for y in range(self.num_cols_and_rows)]
        self.responsibilities = [[0 for x in range(self.num_cols_and_rows)] for y in range(self.num_cols_and_rows)]
        self.availabilities = [[0 for x in range(self.num_cols_and_rows)] for y in range(self.num_cols_and_rows)]
        self.exemplars = []
        self.clusters = [[]]
        self.set_similarities(data_points)
        print(self.similarities)
        print()
        self.set_exemplars(data_points)
        for i in range(self.num_iterations):
            self.set_responsibilities(data_points)
            self.set_availabilities(data_points)
            self.set_exemplars(data_points)
            if i % 10 == 0:
                print(i)
                # print(self.responsibilities)
                # print(self.availabilities)
                # print(self.exemplars)
        print([self.get_exemplar_for(i) for i in range(len(data_points))])
        self.group_points(data_points)
        print(self.clusters)
        print("Number of clusters: " + str(self.get_num_clusters()))
    def get_max_index(self, data_points):
        max_index = 0
        for index in range(1, len(data_points)):
            if data_points[index] >= data_points[max_index]:
                max_index = index
        return max_index
    def get_max(self, data_points):
        if len(data_points) > 0:
            return data_points[self.get_max_index(data_points)]
        return 0
    def min(self, num1, num2):
        if num1 < num2:
            return num1
        return num2
    def set_similarity(self, data_points, row, col):
        self.similarities[row][col] = -(pow(data_points[row][0] - data_points[col][0], 2) + pow(data_points[row][1] - data_points[col][1], 2))
    def set_similarities(self, data_points):
        similarity_values = []
        for row in range(0, len(data_points)):
            for col in range(0, len(data_points)):
                self.set_similarity(data_points, row, col)
        for row in range(0, len(data_points)):
            for col in range(0, len(data_points)):
                if row == col:
                    break
                similarity_values.append(self.similarities[row][col])
        similarity_values.sort()
        size = len(data_points) * (len(data_points) - 1) / 2
        if (size % 2 == 0):
            median = (similarity_values[int(size / 2)] + similarity_values[int(size / 2 - 1)]) / 2
        else:
            median = similarity_values[int(size / 2)]
        for i in range(len(data_points)):
            self.similarities[i][i] = int(median)
    def set_responsibility(self, data_points, row, col):
        input_similarity = self.similarities[row][col]
        max_similarities_plus_availabilities = self.get_max([self.similarities[row][x] + self.availabilities[row][x] for x in range(len(data_points)) if x != col])
        self.responsibilities[row][col] = (1 - self.lam) * (input_similarity - max_similarities_plus_availabilities) + self.responsibilities[row][col] * self.lam
    def set_responsibilities(self, data_points):
        for row in range(0, len(data_points)):
            for col in range(0, len(data_points)):
                self.set_responsibility(data_points, row, col)
    def set_availability(self, data_points, row, col):
        availability = 0
        for index in range(0, len(data_points)):
            if index != row and index != col:
                responsibility = self.responsibilities[index][col]
                if responsibility > 0:
                    availability += responsibility
        if row == col:
            self.availabilities[row][col] = (1 - self.lam) * availability + self.availabilities[row][col] * self.lam
        else:
            self.availabilities[row][col] = (1 - self.lam) * self.min(0, self.responsibilities[row][row] + availability) + self.availabilities[row][col] * self.lam
    def set_availabilities(self, data_points):
        for row in range(0, len(data_points)):
            for col in range(0, len(data_points)):
                self.set_availability(data_points, row, col)
    def set_exemplars(self, data_points):
        self.exemplars = []
        for index in range(len(data_points)):
            if self.availabilities[index][index] + self.responsibilities[index][index] > 0:
                self.exemplars.append(index)
    def get_exemplar_for(self, point):
        candidate_similarities = []
        for i in range(len(self.exemplars)):
            candidate_similarities.append(self.similarities[point][self.exemplars[i]])
        return self.exemplars[self.get_max_index(candidate_similarities)]
    def group_points(self, data_points):
        exemplars_for_points = [self.get_exemplar_for(i) for i in range(len(data_points))]
        self.clusters = [[]]
        self.clusters[0].append(0)
        for i in range(1, len(exemplars_for_points)):
            for j in range(len(self.clusters)):
                if exemplars_for_points[i] == exemplars_for_points[self.clusters[j][0]]:
                    self.clusters[j].append(i)
                    break
                elif j == len(self.clusters) - 1:
                    self.clusters.append([i])
    def get_num_clusters(self):
        return len(self.clusters)