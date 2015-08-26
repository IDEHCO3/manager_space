CREATE TABLE malha_2013.space_boundary(
	id SERIAL PRIMARY KEY,
	name CHARACTER VARYING (255),
	type CHARACTER VARYING (255),
	geom geometry(MultiPolygon, 4326)
);

CREATE TABLE malha_2013.space_boundary_space_boundary(
	parent INTEGER NOT NULL,
	child INTEGER NOT NULL
);