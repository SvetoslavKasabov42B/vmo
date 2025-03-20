class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print("Връхът вече съществува.")

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            print("Един от върховете не съществува.")

    def search_vertex(self, vertex):
        return vertex in self.graph

    def search_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            return vertex2 in self.graph[vertex1]
        return False

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
        else:
            print("Връхът не съществува.")

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        else:
            print("Дъгата не съществува.")

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")


def menu():
    graph = Graph()
    while True:
        print("\n1. Добавяне на връх")
        print("2. Добавяне на дъга")
        print("3. Търсене на връх")
        print("4. Търсене на дъга")
        print("5. Изтриване на връх")
        print("6. Изтриване на дъга")
        print("7. Визуализация на графа")
        print("8. Изход")
        choice = input("Изберете опция: ")

        if choice == '1':
            vertex = input("Въведете връх: ")
            graph.add_vertex(vertex)
        elif choice == '2':
            vertex1 = input("Въведете първи връх: ")
            vertex2 = input("Въведете втори връх: ")
            graph.add_edge(vertex1, vertex2)
        elif choice == '3':
            vertex = input("Въведете връх: ")
            print("Връхът съществува." if graph.search_vertex(vertex) else "Връхът не съществува.")
        elif choice == '4':
            vertex1 = input("Въведете първи връх: ")
            vertex2 = input("Въведете втори връх: ")
            print("Дъгата съществува." if graph.search_edge(vertex1, vertex2) else "Дъгата не съществува.")
        elif choice == '5':
            vertex = input("Въведете връх: ")
            graph.delete_vertex(vertex)
        elif choice == '6':
            vertex1 = input("Въведете първи връх: ")
            vertex2 = input("Въведете втори връх: ")
            graph.delete_edge(vertex1, vertex2)
        elif choice == '7':
            graph.display()
        elif choice == '8':
            break
        else:
            print("Невалиден избор.")

if __name__ == "__main__":
    menu()
