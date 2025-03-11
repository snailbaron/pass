genrule(
    name = "download_planet_osm",
    srcs = ["@planet_osm_torrent//file"],
    outs = ["planet_osm.pbf"],
    cmd = "./$(location //src/download) -i \"$(location @planet_osm_torrent//file)\" -o . && mv planet-250303.osm.pbf \"$@\"",
    tools = ["//src/download"],
)
