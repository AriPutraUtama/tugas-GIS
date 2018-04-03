import mapnik
m = mapnik.Map(3840,2160)
m.background = mapnik.Color('steelblue')
# MAP 1 DUNIA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#7FFF00')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Ari',s)
ds = mapnik.Shapefile(file="countries/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Ari')
m.layers.append(layer)
# BATAS AKHIR MAP 1 DUNIA

# MAP 2 Negara Afganistan 
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#D2691E')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Ari2',s)
ds = mapnik.Shapefile(file="afganistan/map.shp")
layer = mapnik.Layer('Afganistan')
layer.datasource = ds
layer.styles.append('Ari2')
m.layers.append(layer)
# BATAS AKHIR MAP 2 negara Afganistan

# 
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#00FFFF')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Turquoise'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Ari3',s)
ds = mapnik.Shapefile(file="canada/map.shp")
layer = mapnik.Layer('canada')
layer.datasource = ds
layer.styles.append('Ari3')
m.layers.append(layer)

#

s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FAEBD7')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Turquoise'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Ari4',s)
ds = mapnik.Shapefile(file="germany/map.shp")
layer = mapnik.Layer('germany')
layer.datasource = ds
layer.styles.append('Ari4')
m.layers.append(layer)

#

s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FF69B4')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Turquoise'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Ari5',s)
ds = mapnik.Shapefile(file="indonesia/map.shp")
layer = mapnik.Layer('indonesia')
layer.datasource = ds
layer.styles.append('Ari5')
m.layers.append(layer)

#

s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#A52A2A')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Turquoise'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Ari6',s)
ds = mapnik.Shapefile(file="turkey/map.shp")
layer = mapnik.Layer('turkey')
layer.datasource = ds
layer.styles.append('Ari6')
m.layers.append(layer)


m.zoom_all()
mapnik.render_to_file(m,'world.jpeg','jpeg')
print "rendered image to 'world.jpeg'"
