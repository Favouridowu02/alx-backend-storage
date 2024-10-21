-- A SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
CREATE VIEW fans AS SELECT origin, nb_fans FROM metal_bands;
