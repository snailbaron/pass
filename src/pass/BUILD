load("@rules_cc//cc:cc_binary.bzl", "cc_binary")

cc_binary(
    name = "pass",
    srcs = [
        "main.cpp",
    ],
    #data = ["@planet-osm//file"],
    deps = ["//deps:libosmium"],
)
