from HW1.maps import Parser
from HW1.algorithms import Search
from HW1.algorithms import Search


def hline():
    print(35 * '-')


p = Parser()
m = p.get_map(3)

# print(m.goals)
# print(m.width)
# print(m.height)
# print(m.me)
# print(m.map_array)
# print(m.is_valid_cell(0, 0))
# print(m.is_valid_cell(3,0))
# print(m.get_successors(2,1))
# m.draw()

# Run algorithms
maps = p.get_all_maps()
s = Search()
for mp in maps:
    print(mp, '\n')
    # print('Footprints:', s.bfs(mp))
    # mp.draw(algorithm=s.bfs)
    # hline()
    # print('Footprints:', s.dfs(mp))
    # mp.draw(algorithm=s.dfs)
    # hline()
    # print('Footprints:', s.bfs(mp))
    # mp.draw(algorithm=s.bfs)
    # hline()
    print('Footprints:', s.a_star(mp, []))
    mp.draw(algorithm=s.a_star, heuristics='heuristics')
    hline()
    print('\n')
