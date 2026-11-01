---
records:
    - id: QNE8Y1E3EZ
      kind: monograph
      title: Introduction to Smooth Manifolds
      creators:
        - name: John M. Lee
          role: author
      date: "2003"
      msc:
        - code: 53-02
          from: zbmath_search
        - code: 58-02
          from: zbmath_search
        - code: 57-02
          from: zbmath_search
        - code: 53Cxx
          from: zbmath_search
        - code: 57Rxx
          from: zbmath_search
        - code: 58Axx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2003"
          ids:
            doi:
                - 10.1007/978-0-387-21752-9
                - 10.1007/978-1-4419-9982-5
            zbl: "1030.53001"
            zbl_id: "1821399"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2003"
              ids:
                isbn:
                    - "9780387954486"
                    - "9780387217529"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2012"
              ids:
                isbn:
                    - "9781441999818"
                    - "9781441999825"
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
          native_id: 10.1007/978-0-387-21752-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-9982-5
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1821399"
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
          by: m2 v0.6.14 scope/1
          note: from in to in
---
