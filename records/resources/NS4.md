---
records:
    - id: NS4VAQJ76P
      kind: monograph
      title: Big Queues
      creators:
        - name: Ayalvadi Ganesh
          role: author
        - name: Neil O’Connell
          role: author
        - name: Damon Wischik
          role: author
      date: "2004"
      msc:
        - code: 60-01
          from: zbmath_search
        - code: 60K25
          from: zbmath_search
        - code: 90B22
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2004"
          ids:
            doi: 10.1007/978-3-540-39889-9
            zbl: "1044.60001"
            zbl_id: "2061720"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2004"
              ids:
                isbn:
                    - "9783540209126"
                    - "9783540398899"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-39889-9
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "2061720"
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
