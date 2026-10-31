---
records:
    - id: EYVN8ZHPSZ
      kind: monograph
      title: Linear Algebra
      creators:
        - name: Serge Lang
          role: author
      date: "1987"
      msc:
        - code: 15-01
          from: zbmath_search
        - code: 65F05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 3rd edition
          language: en
          date: "1987"
          ids:
            doi: 10.1007/978-1-4757-1949-9
            zbl: "0618.15001"
            zbl_id: "4002273"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1987"
              ids:
                isbn:
                    - "9781441930811"
                    - "9781475719499"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-1949-9
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "4002273"
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
