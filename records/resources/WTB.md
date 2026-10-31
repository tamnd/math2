---
records:
    - id: WTB0HKRW84
      kind: problem-set
      title: Kvant 1986, no. 4
      date: "1986"
      expressions:
        - key: e1
          kind: edition
          date: "1986"
          structure: WTB0HKRW84/e1.json
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
          native_id: 1986-4
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: WTBHZC3CWG
      kind: monograph
      title: More Calculus of a Single Variable
      creators:
        - name: Peter R. Mercer
          role: author
      date: "2014"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 00A05
          from: zbmath_search
        - code: 26Axx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2014"
          ids:
            doi: 10.1007/978-1-4939-1926-0
            zbl: "1305.26006"
            zbl_id: "6340689"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2014"
              ids:
                isbn:
                    - "9781493919253"
                    - "9781493919260"
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
          native_id: 10.1007/978-1-4939-1926-0
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "6340689"
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
