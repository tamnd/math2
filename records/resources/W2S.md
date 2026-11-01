---
records:
    - id: W2S14NMHXZ
      kind: monograph
      title: Probability Theory and Stochastic Processes
      creators:
        - name: Pierre Brémaud
          role: author
      date: "2020"
      msc:
        - code: 60-01
          from: zbmath_search
        - code: 60Gxx
          from: zbmath_search
        - code: 60Hxx
          from: zbmath_search
        - code: 60Kxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2020"
          ids:
            doi: 10.1007/978-3-030-40183-2
            zbl: "1445.60001"
            zbl_id: "7188888"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2020"
              ids:
                isbn:
                    - "9783030401825"
                    - "9783030401832"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-40183-2
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "7188888"
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
