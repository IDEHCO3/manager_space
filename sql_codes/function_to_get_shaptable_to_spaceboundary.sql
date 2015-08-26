CREATE OR REPLACE FUNCTION malha_2013.to_space_boundary( id_parent integer) RETURNS integer AS $$
DECLARE
	rec  RECORD;
	seq  Integer;
BEGIN
	FOR REC IN SELECT * FROM malha_2013."33mue250gc_sir" LOOP
		BEGIN
			seq = nextval('malha_2013.space_boundary_id_seq');
			INSERT INTO malha_2013.space_boundary(id, name, type, geocode, geom) VALUES (seq ,REC.nm_municip, 'municipio', REC.cd_geocmu, REC.geom);
			INSERT INTO malha_2013.space_boundary_space_boundary(parent, child) VALUES(id_parent, seq);

		EXCEPTION WHEN OTHERS THEN
			RETURN -1;
		END;
	END LOOP;
	RETURN 1;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION malha_2013.estado_to_space_boundary() RETURNS integer AS $$
DECLARE
	rec  RECORD;
BEGIN
	FOR REC IN SELECT * FROM malha_2013."33ufe250gc_sir" LOOP
		INSERT INTO malha_2013.space_boundary( name, type, geocode, geom) VALUES (REC.nm_estado, 'estado', REC.cd_geocuf, REC.geom);
	END LOOP;
	RETURN 1;
EXCEPTION WHEN unique_violation THEN
	RETURN -1;
END;
$$ LANGUAGE plpgsql;
