---
records:
    - id: Y1EEB7KZ2H
      kind: monograph
      title: Essentials of Integration Theory for Analysis
      creators:
        - name: Daniel W. Stroock
          role: author
      date: "2011"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 26A42
          from: zbmath_search
        - code: 28-01
          from: zbmath_search
        - code: 28A25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2011"
          ids:
            doi:
                - 10.1007/978-1-4614-1135-2
                - 10.1007/978-3-030-58478-8
            zbl: "1228.26001"
            zbl_id: "5936209"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2011"
              ids:
                isbn:
                    - "9781461411345"
                    - "9781461411352"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2020"
              ids:
                isbn:
                    - "9783030584771"
                    - "9783030584788"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-1135-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-58478-8
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "5936209"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
