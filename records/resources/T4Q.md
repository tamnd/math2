---
records:
    - id: T4Q8JR41WH
      kind: monograph
      title: Number Fields
      creators:
        - name: Daniel A. Marcus
          role: author
      date: "1977"
      msc:
        - code: 11-02
          from: zbmath_search
        - code: 11-01
          from: zbmath_search
        - code: 11R21
          from: zbmath_search
        - code: 11R04
          from: zbmath_search
        - code: 11R23
          from: zbmath_search
        - code: 11R27
          from: zbmath_search
        - code: 11R37
          from: zbmath_search
        - code: 11R42
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1977"
          ids:
            doi:
                - 10.1007/978-1-4684-9356-6
                - 10.1007/978-3-319-90233-3
            zbl: "0383.12001"
            zbl_id: "3595278"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1977"
              ids:
                isbn:
                    - "9780387902791"
                    - "9781468493566"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783319902326"
                    - "9783319902333"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9356-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-90233-3
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3595278"
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
