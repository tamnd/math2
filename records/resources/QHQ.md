---
records:
    - id: QHQVVWSA14
      kind: monograph
      title: Cellular Automata and Groups
      creators:
        - name: Tullio Ceccherini-Silberstein
          role: author
        - name: Michel Coornaert
          role: author
      date: "2010"
      msc:
        - code: 37-02
          from: zbmath_search
        - code: 37B15
          from: zbmath_search
        - code: 68Q80
          from: zbmath_search
        - code: 20F65
          from: zbmath_search
        - code: 20M35
          from: zbmath_search
        - code: 68Q70
          from: zbmath_search
        - code: 20-02
          from: zbmath_search
        - code: 68-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010"
          ids:
            doi:
                - 10.1007/978-3-031-43328-3
                - 10.1007/978-3-642-14034-1
            zbl: "1218.37004"
            zbl_id: "5771641"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2023"
              ids:
                isbn:
                    - "9783031433276"
                    - "9783031433283"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2010"
              ids:
                isbn:
                    - "9783642140334"
                    - "9783642140341"
              access:
                class: record
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-031-43328-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-14034-1
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "5771641"
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
