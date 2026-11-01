---
records:
    - id: ZHD29F48AF
      kind: monograph
      title: Real Mathematical Analysis
      creators:
        - name: Charles Chapman Pugh
          role: author
      date: "2002"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 28-01
          from: zbmath_search
        - code: 46-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2002"
          ids:
            doi:
                - 10.1007/978-0-387-21684-3
                - 10.1007/978-3-319-17771-7
            zbl: "1003.26001"
            zbl_id: "1749058"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2002"
              ids:
                isbn:
                    - "9781441929419"
                    - "9780387216843"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319177700"
                    - "9783319177717"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-21684-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-17771-7
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1749058"
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
    - id: ZHDVCXRE23
      kind: problem-set
      title: KöMaL Problems in Mathematics, March 2016
      creators:
        - name: KöMaL editorial board
          role: editor
      date: 2016-03
      msc:
        - code: 00A07
          from: komal
        - code: 97U40
          from: komal
      expressions:
        - key: e1
          kind: edition
          language: en
          date: 2016-03
          structure: ZHDVCXRE23/e1.json
      relations:
        - kind: part_of
          to: 4T7QDPBW1N
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: komal
          snapshot: blake3:3658e660acc064da2c1a894c81d6f74fed1bee98fd8e0b9c468109c4c7e40452
          native_id: 2016-03
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
