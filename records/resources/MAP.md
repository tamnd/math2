---
records:
    - id: MAPS9GQ2CW
      kind: monograph
      title: Transformation Geometry
      creators:
        - name: George E. Martin
          role: author
      date: "1982"
      msc:
        - code: 51-01
          from: zbmath_search
        - code: 51M05
          from: zbmath_search
        - code: 51M20
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1982"
          ids:
            doi: 10.1007/978-1-4612-5680-9
            zbl: "0484.51001"
            zbl_id: "3760882"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1982"
              ids:
                isbn:
                    - "9781461256823"
                    - "9781461256809"
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
          native_id: 10.1007/978-1-4612-5680-9
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3760882"
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
