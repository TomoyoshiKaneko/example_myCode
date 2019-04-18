using CSV, Gadfly, DataFrames, DataFramesMeta, Statistics, HypothesisTests, Cairo, Fontconfig

# scaning data, make sure table's format
dat = CSV.read("datasets/ladybirds_morph_colour.csv")
describe(dat)
by(dat, :Habitat, :number => mean)
by(dat, [:Habitat, :morph_colour], lady = :number => sum)
by(dat, [:Habitat, :morph_colour], lady = :number => mean)
by(dat, [:Habitat, :morph_colour], lady = :number => var)

# get the data as graph
draw(PDF("fig/ladybird_1.pdf", 10cm, 8cm),plot(dat, y = :numberGeom.bar))
draw(PDF("fig/ladybird_2.pdf", 10cm, 8cm),plot(dat, y = :numberGeom.bar))

# each group's bar graph
draw(PDF("fig/ladybird_3", 10cm, 8cm),plot(dat,xgroup = :Habitat, x = :morph_colour, y = :number, color = :morph_colour, Scale.y_continuous(minvalue = 0),Geom.subplot_grid(Geom.bar())))

# 2x2divided-table: Habitat x morph_colour = 2 x 2 = 4th
cont = by(dat, [:Habitat, :morph_colour], lady=:number => sum)
res = ChisqTest(reshape(cont[:,:lady], 2,2))

draw(PDF("fig/ladybird_4.pdf", 10cm, 8cm),plot(dat, xgroup = :Habitat, ))
