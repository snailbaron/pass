load("@rules_cc//cc:cc_library.bzl", "cc_library")

cc_library(
    name = "protozero",
    hdrs = glob(["protozero/include/protozero/**/*.hpp"]),
    strip_include_prefix = "protozero/include",
)

cc_library(
    name = "libosmium",
    hdrs = glob(["libosmium/include/osmium/**/*.hpp"]),
    strip_include_prefix = "libosmium/include",
    visibility = ["//visibility:public"],
    deps = [
        "protozero",
        "@zlib",
    ],
)
