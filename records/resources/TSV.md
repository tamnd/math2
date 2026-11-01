---
records:
    - id: TSVNF88HE3
      kind: monograph
      title: Riemannian Geometry
      creators:
        - name: Peter Petersen
          role: author
      date: "1998"
      msc:
        - code: 53-01
          from: zbmath_search
        - code: 53C20
          from: zbmath_search
        - code: 53Cxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1998"
          ids:
            doi:
                - 10.1007/978-1-4757-6434-5
                - 10.1007/978-3-319-26654-1
            zbl: "0914.53001"
            zbl_id: "1101836"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1998"
              ids:
                isbn:
                    - "9781475764369"
                    - "9781475764345"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2016"
              ids:
                isbn:
                    - "9783319266527"
                    - "9783319266541"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-6434-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-26654-1
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1101836"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
