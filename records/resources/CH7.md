---
records:
    - id: CH7NN7YSK5
      kind: monograph
      title: Much Ado About Calculus
      creators:
        - name: Robert L. Wilson
          role: author
      date: "1979"
      msc:
        - code: 26-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1979"
          ids:
            doi: 10.1007/978-1-4615-9644-8
            zbl: "0412.26001"
            zbl_id: "3639921"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1979"
              ids:
                isbn:
                    - "9781461596462"
                    - "9781461596448"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.17 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4615-9644-8
          level: work
        - source: zbmath_search
          snapshot: blake3:ba52b67aca79888bd54f4ac0d57bd446df8c82ca03dd9e92e0bc9db1402905ce
          native_id: "3639921"
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
