# https://s2sphere.readthedocs.io/en/latest/quickstart.html
import s2sphere

r = s2sphere.RegionCoverer()
p1 = s2sphere.LatLng.from_degrees(33, -122)
p2 = s2sphere.LatLng.from_degrees(33.1, -122.1)
cell_ids = r.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))
print(len(cell_ids))

# expect-output-to-have: 8