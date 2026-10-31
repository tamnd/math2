---
records:
    - id: JT1A0HN6AZ
      kind: problem-set
      title: Kvant 1979, no. 2
      date: "1979"
      expressions:
        - key: e1
          kind: edition
          date: "1979"
          structure: JT1A0HN6AZ/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1979-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: JT1XRA6X4P
      kind: monograph
      title: Introduction to Lie Algebras
      creators:
        - name: Karin Erdmann
          role: author
        - name: Mark J. Wildon
          role: author
      date: "2006"
      msc:
        - code: 17-01
          from: zbmath_search
        - code: 17B05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2006"
          ids:
            doi: 10.1007/1-84628-490-2
            zbl: "1139.17001"
            zbl_id: "5031712"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2006"
              ids:
                isbn:
                    - "9781846280405"
                    - "9781846284908"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/1-84628-490-2
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "5031712"
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
