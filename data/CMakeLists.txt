macro(download_file_target)
    set(options "")
    set(oneValueArgs TARGET URL MD5 FILE)
    set(multiValueArgs "")
    cmake_parse_arguments(arg_download_file_target
        "${options}" "${oneValueArgs}" "${multiValueArgs}"
        ${ARGN}
    )

    set(output_file "${CMAKE_CURRENT_BINARY_DIR}/${arg_download_file_target_FILE}")
    add_custom_command(
        COMMENT "downloading ${arg_download_file_target_URL} to ${arg_download_file_target_FILE}"
        OUTPUT "${output_file}"
        COMMAND "${PROJECT_SOURCE_DIR}/src/download_file/download_file"
            --url "${arg_download_file_target_URL}"
            --md5 "${arg_download_file_target_MD5}"
            --output "${output_file}"
        DEPENDS download_file
    )

    add_custom_target(
        ${arg_download_file_target_TARGET} ALL
        DEPENDS "${output_file}"
    )
endmacro()

download_file_target(
    TARGET download_planet_osm
    URL https://planet.openstreetmap.org/pbf/planet-250303.osm.pbf
    MD5 478360c346fbbfb5c5a935f636bf903c
    FILE planet-250303.osm.pbf
)
