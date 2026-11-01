---
records:
    - id: 3FAWV8EA4E
      kind: monograph
      title: Sobolev Gradients and Differential Equations
      creators:
        - name: J.W. Neuberger
          role: author
      date: "1997"
      msc:
        - code: 35-02
          from: zbmath_search
        - code: 65N99
          from: zbmath_search
        - code: 35A15
          from: zbmath_search
        - code: 35A35
          from: zbmath_search
        - code: 65J15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1997"
          ids:
            doi:
                - 10.1007/978-3-642-04041-2
                - 10.1007/bfb0092831
            zbl: "0935.35002"
            zbl_id: "1077208"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2010"
              ids:
                isbn:
                    - "9783642040405"
                    - "9783642040412"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1997"
              ids:
                isbn:
                    - "9783540635376"
                    - "9783540695943"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-04041-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0092831
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1077208"
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
