from collections import defaultdict
import re

best_path = []

def dfs_edges(current_node, graph, current_path, visited_edges, countreb):
    global best_path
    
    if len(current_path) > len(best_path):
        print(current_path)
        best_path = list(current_path)
        
    for idx, frag in graph[current_node]:
        if idx not in visited_edges:
            visited_edges.add(idx)
            current_path.append(frag)
            dfs_edges(frag[-countreb:], graph, current_path, visited_edges, countreb)
            current_path.pop()
            visited_edges.remove(idx)

def practice_longest_path():
    dia = input("Обери яким способом отримати фрагменти\nНапиши фрагменти\nНапиши шлях до фрагментів\n->").strip('\"\'')
    if re.search( r'[/\\]', dia):
        with open(dia, "r", encoding="utf-8") as file:
            fragments = re.sub(r'[^0-9 \n]', '', file.read()).split()
    else:
        fragments = re.sub(r'[^0-9 \n]', '', dia).split()
    countreb = int(input("Напиши скільки враховувати кінцівок цифр для пошуку однорядкового цифрового пазлу\n->"))
    graph = defaultdict(list)
    for i, frag in enumerate(fragments):
        graph[frag[:countreb]].append((i, frag))
        
    print(f"Починаємо пошук найдовшого шляху з вузла '12'...")
    for all_node_for in list(graph):
        dfs_edges(all_node_for, graph, [], set(), countreb)
    
    print("\nНайдовший знайдений ланцюжок:")
    print(" -> ".join(best_path))
    print(f"Використано фрагментів: {len(best_path)} з {len(fragments)}")
    if best_path:
        result_str = best_path[0]
        for frag in best_path[1:]:
            result_str += frag[countreb:]
            
        print("\nВідповідь склеїні:")
        print(result_str)
        print("\nВідповідь всього цифр:")
        print(len(result_str))
if __name__ == "__main__":
    practice_longest_path()
    input("\nНатисни Enter щоб продовжити...")