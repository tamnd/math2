---
records:
    - id: DM7XS043AN
      kind: monograph
      title: Inverse Problems for Partial Differential Equations
      creators:
        - name: Victor Isakov
          role: author
      date: "1998"
      msc:
        - code: 35R30
          from: zbmath_search
        - code: 35-02
          from: zbmath_search
        - code: 35J15
          from: zbmath_search
        - code: 35K30
          from: zbmath_search
        - code: 35P25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1998"
          ids:
            doi:
                - 10.1007/978-1-4899-0030-2
                - 10.1007/978-3-319-51658-5
            zbl: "0908.35134"
            zbl_id: "1113140"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1998"
              ids:
                isbn:
                    - "9781489900326"
                    - "9781489900302"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2017"
              ids:
                isbn:
                    - "9783319516578"
                    - "9783319516585"
              access:
                class: record
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4899-0030-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-51658-5
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1113140"
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
